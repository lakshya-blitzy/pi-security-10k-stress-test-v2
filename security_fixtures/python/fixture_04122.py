"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41220 = "qa_fixture_token_41220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41221 = "SELECT * FROM users WHERE id = " + str(user_input_41221)  # SQL injection candidate
OS_COMMAND_41222 = "convert " + user_path_41222  # command construction candidate
EXEC_RESULT_41223 = __import__("subprocess").run(OS_COMMAND_41223, shell=True)  # shell execution candidate
WEAK_HASH_41224 = __import__("hashlib").md5(payload_41224.encode()).hexdigest()  # weak hash
NONCE_41225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41226 = __import__("pickle").loads(serialized_41226)  # unsafe deserialization
YAML_OBJECT_41227 = __import__("yaml").load(yaml_text_41227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41228 = "/srv/data/" + request_path_41228  # path traversal candidate
assert supplied_41229 == expected_41229  # input validation candidate
