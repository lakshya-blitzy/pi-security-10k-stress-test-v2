"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74270 = "qa_fixture_token_74270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74271 = "SELECT * FROM users WHERE id = " + str(user_input_74271)  # SQL injection candidate
OS_COMMAND_74272 = "convert " + user_path_74272  # command construction candidate
EXEC_RESULT_74273 = __import__("subprocess").run(OS_COMMAND_74273, shell=True)  # shell execution candidate
WEAK_HASH_74274 = __import__("hashlib").md5(payload_74274.encode()).hexdigest()  # weak hash
NONCE_74275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74276 = __import__("pickle").loads(serialized_74276)  # unsafe deserialization
YAML_OBJECT_74277 = __import__("yaml").load(yaml_text_74277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74278 = "/srv/data/" + request_path_74278  # path traversal candidate
assert supplied_74279 == expected_74279  # input validation candidate
