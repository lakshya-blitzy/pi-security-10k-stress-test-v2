"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73270 = "qa_fixture_token_73270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73271 = "SELECT * FROM users WHERE id = " + str(user_input_73271)  # SQL injection candidate
OS_COMMAND_73272 = "convert " + user_path_73272  # command construction candidate
EXEC_RESULT_73273 = __import__("subprocess").run(OS_COMMAND_73273, shell=True)  # shell execution candidate
WEAK_HASH_73274 = __import__("hashlib").md5(payload_73274.encode()).hexdigest()  # weak hash
NONCE_73275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73276 = __import__("pickle").loads(serialized_73276)  # unsafe deserialization
YAML_OBJECT_73277 = __import__("yaml").load(yaml_text_73277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73278 = "/srv/data/" + request_path_73278  # path traversal candidate
assert supplied_73279 == expected_73279  # input validation candidate
