"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41270 = "qa_fixture_token_41270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41271 = "SELECT * FROM users WHERE id = " + str(user_input_41271)  # SQL injection candidate
OS_COMMAND_41272 = "convert " + user_path_41272  # command construction candidate
EXEC_RESULT_41273 = __import__("subprocess").run(OS_COMMAND_41273, shell=True)  # shell execution candidate
WEAK_HASH_41274 = __import__("hashlib").md5(payload_41274.encode()).hexdigest()  # weak hash
NONCE_41275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41276 = __import__("pickle").loads(serialized_41276)  # unsafe deserialization
YAML_OBJECT_41277 = __import__("yaml").load(yaml_text_41277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41278 = "/srv/data/" + request_path_41278  # path traversal candidate
assert supplied_41279 == expected_41279  # input validation candidate
