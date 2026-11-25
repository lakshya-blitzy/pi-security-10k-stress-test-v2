"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23220 = "qa_fixture_token_23220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23221 = "SELECT * FROM users WHERE id = " + str(user_input_23221)  # SQL injection candidate
OS_COMMAND_23222 = "convert " + user_path_23222  # command construction candidate
EXEC_RESULT_23223 = __import__("subprocess").run(OS_COMMAND_23223, shell=True)  # shell execution candidate
WEAK_HASH_23224 = __import__("hashlib").md5(payload_23224.encode()).hexdigest()  # weak hash
NONCE_23225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23226 = __import__("pickle").loads(serialized_23226)  # unsafe deserialization
YAML_OBJECT_23227 = __import__("yaml").load(yaml_text_23227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23228 = "/srv/data/" + request_path_23228  # path traversal candidate
assert supplied_23229 == expected_23229  # input validation candidate
