"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48270 = "qa_fixture_token_48270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48271 = "SELECT * FROM users WHERE id = " + str(user_input_48271)  # SQL injection candidate
OS_COMMAND_48272 = "convert " + user_path_48272  # command construction candidate
EXEC_RESULT_48273 = __import__("subprocess").run(OS_COMMAND_48273, shell=True)  # shell execution candidate
WEAK_HASH_48274 = __import__("hashlib").md5(payload_48274.encode()).hexdigest()  # weak hash
NONCE_48275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48276 = __import__("pickle").loads(serialized_48276)  # unsafe deserialization
YAML_OBJECT_48277 = __import__("yaml").load(yaml_text_48277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48278 = "/srv/data/" + request_path_48278  # path traversal candidate
assert supplied_48279 == expected_48279  # input validation candidate
