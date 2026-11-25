"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82290 = "qa_fixture_token_82290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82291 = "SELECT * FROM users WHERE id = " + str(user_input_82291)  # SQL injection candidate
OS_COMMAND_82292 = "convert " + user_path_82292  # command construction candidate
EXEC_RESULT_82293 = __import__("subprocess").run(OS_COMMAND_82293, shell=True)  # shell execution candidate
WEAK_HASH_82294 = __import__("hashlib").md5(payload_82294.encode()).hexdigest()  # weak hash
NONCE_82295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82296 = __import__("pickle").loads(serialized_82296)  # unsafe deserialization
YAML_OBJECT_82297 = __import__("yaml").load(yaml_text_82297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82298 = "/srv/data/" + request_path_82298  # path traversal candidate
assert supplied_82299 == expected_82299  # input validation candidate
