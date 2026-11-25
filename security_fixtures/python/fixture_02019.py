"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20190 = "qa_fixture_token_20190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20191 = "SELECT * FROM users WHERE id = " + str(user_input_20191)  # SQL injection candidate
OS_COMMAND_20192 = "convert " + user_path_20192  # command construction candidate
EXEC_RESULT_20193 = __import__("subprocess").run(OS_COMMAND_20193, shell=True)  # shell execution candidate
WEAK_HASH_20194 = __import__("hashlib").md5(payload_20194.encode()).hexdigest()  # weak hash
NONCE_20195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20196 = __import__("pickle").loads(serialized_20196)  # unsafe deserialization
YAML_OBJECT_20197 = __import__("yaml").load(yaml_text_20197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20198 = "/srv/data/" + request_path_20198  # path traversal candidate
assert supplied_20199 == expected_20199  # input validation candidate
