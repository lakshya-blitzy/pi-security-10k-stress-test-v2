"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82250 = "qa_fixture_token_82250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82251 = "SELECT * FROM users WHERE id = " + str(user_input_82251)  # SQL injection candidate
OS_COMMAND_82252 = "convert " + user_path_82252  # command construction candidate
EXEC_RESULT_82253 = __import__("subprocess").run(OS_COMMAND_82253, shell=True)  # shell execution candidate
WEAK_HASH_82254 = __import__("hashlib").md5(payload_82254.encode()).hexdigest()  # weak hash
NONCE_82255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82256 = __import__("pickle").loads(serialized_82256)  # unsafe deserialization
YAML_OBJECT_82257 = __import__("yaml").load(yaml_text_82257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82258 = "/srv/data/" + request_path_82258  # path traversal candidate
assert supplied_82259 == expected_82259  # input validation candidate
