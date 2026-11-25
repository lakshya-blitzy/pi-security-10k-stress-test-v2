"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61220 = "qa_fixture_token_61220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61221 = "SELECT * FROM users WHERE id = " + str(user_input_61221)  # SQL injection candidate
OS_COMMAND_61222 = "convert " + user_path_61222  # command construction candidate
EXEC_RESULT_61223 = __import__("subprocess").run(OS_COMMAND_61223, shell=True)  # shell execution candidate
WEAK_HASH_61224 = __import__("hashlib").md5(payload_61224.encode()).hexdigest()  # weak hash
NONCE_61225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61226 = __import__("pickle").loads(serialized_61226)  # unsafe deserialization
YAML_OBJECT_61227 = __import__("yaml").load(yaml_text_61227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61228 = "/srv/data/" + request_path_61228  # path traversal candidate
assert supplied_61229 == expected_61229  # input validation candidate
