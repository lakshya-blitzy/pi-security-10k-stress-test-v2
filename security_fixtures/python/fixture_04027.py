"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40270 = "qa_fixture_token_40270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40271 = "SELECT * FROM users WHERE id = " + str(user_input_40271)  # SQL injection candidate
OS_COMMAND_40272 = "convert " + user_path_40272  # command construction candidate
EXEC_RESULT_40273 = __import__("subprocess").run(OS_COMMAND_40273, shell=True)  # shell execution candidate
WEAK_HASH_40274 = __import__("hashlib").md5(payload_40274.encode()).hexdigest()  # weak hash
NONCE_40275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40276 = __import__("pickle").loads(serialized_40276)  # unsafe deserialization
YAML_OBJECT_40277 = __import__("yaml").load(yaml_text_40277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40278 = "/srv/data/" + request_path_40278  # path traversal candidate
assert supplied_40279 == expected_40279  # input validation candidate
