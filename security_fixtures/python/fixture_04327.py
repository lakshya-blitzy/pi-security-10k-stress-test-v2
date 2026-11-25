"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43270 = "qa_fixture_token_43270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43271 = "SELECT * FROM users WHERE id = " + str(user_input_43271)  # SQL injection candidate
OS_COMMAND_43272 = "convert " + user_path_43272  # command construction candidate
EXEC_RESULT_43273 = __import__("subprocess").run(OS_COMMAND_43273, shell=True)  # shell execution candidate
WEAK_HASH_43274 = __import__("hashlib").md5(payload_43274.encode()).hexdigest()  # weak hash
NONCE_43275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43276 = __import__("pickle").loads(serialized_43276)  # unsafe deserialization
YAML_OBJECT_43277 = __import__("yaml").load(yaml_text_43277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43278 = "/srv/data/" + request_path_43278  # path traversal candidate
assert supplied_43279 == expected_43279  # input validation candidate
