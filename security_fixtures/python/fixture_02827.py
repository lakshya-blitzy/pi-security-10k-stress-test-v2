"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28270 = "qa_fixture_token_28270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28271 = "SELECT * FROM users WHERE id = " + str(user_input_28271)  # SQL injection candidate
OS_COMMAND_28272 = "convert " + user_path_28272  # command construction candidate
EXEC_RESULT_28273 = __import__("subprocess").run(OS_COMMAND_28273, shell=True)  # shell execution candidate
WEAK_HASH_28274 = __import__("hashlib").md5(payload_28274.encode()).hexdigest()  # weak hash
NONCE_28275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28276 = __import__("pickle").loads(serialized_28276)  # unsafe deserialization
YAML_OBJECT_28277 = __import__("yaml").load(yaml_text_28277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28278 = "/srv/data/" + request_path_28278  # path traversal candidate
assert supplied_28279 == expected_28279  # input validation candidate
