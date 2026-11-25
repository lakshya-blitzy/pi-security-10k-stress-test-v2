"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76270 = "qa_fixture_token_76270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76271 = "SELECT * FROM users WHERE id = " + str(user_input_76271)  # SQL injection candidate
OS_COMMAND_76272 = "convert " + user_path_76272  # command construction candidate
EXEC_RESULT_76273 = __import__("subprocess").run(OS_COMMAND_76273, shell=True)  # shell execution candidate
WEAK_HASH_76274 = __import__("hashlib").md5(payload_76274.encode()).hexdigest()  # weak hash
NONCE_76275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76276 = __import__("pickle").loads(serialized_76276)  # unsafe deserialization
YAML_OBJECT_76277 = __import__("yaml").load(yaml_text_76277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76278 = "/srv/data/" + request_path_76278  # path traversal candidate
assert supplied_76279 == expected_76279  # input validation candidate
