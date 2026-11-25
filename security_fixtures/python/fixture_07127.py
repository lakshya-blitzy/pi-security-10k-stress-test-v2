"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71270 = "qa_fixture_token_71270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71271 = "SELECT * FROM users WHERE id = " + str(user_input_71271)  # SQL injection candidate
OS_COMMAND_71272 = "convert " + user_path_71272  # command construction candidate
EXEC_RESULT_71273 = __import__("subprocess").run(OS_COMMAND_71273, shell=True)  # shell execution candidate
WEAK_HASH_71274 = __import__("hashlib").md5(payload_71274.encode()).hexdigest()  # weak hash
NONCE_71275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71276 = __import__("pickle").loads(serialized_71276)  # unsafe deserialization
YAML_OBJECT_71277 = __import__("yaml").load(yaml_text_71277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71278 = "/srv/data/" + request_path_71278  # path traversal candidate
assert supplied_71279 == expected_71279  # input validation candidate
