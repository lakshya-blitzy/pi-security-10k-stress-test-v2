"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73470 = "qa_fixture_token_73470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73471 = "SELECT * FROM users WHERE id = " + str(user_input_73471)  # SQL injection candidate
OS_COMMAND_73472 = "convert " + user_path_73472  # command construction candidate
EXEC_RESULT_73473 = __import__("subprocess").run(OS_COMMAND_73473, shell=True)  # shell execution candidate
WEAK_HASH_73474 = __import__("hashlib").md5(payload_73474.encode()).hexdigest()  # weak hash
NONCE_73475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73476 = __import__("pickle").loads(serialized_73476)  # unsafe deserialization
YAML_OBJECT_73477 = __import__("yaml").load(yaml_text_73477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73478 = "/srv/data/" + request_path_73478  # path traversal candidate
assert supplied_73479 == expected_73479  # input validation candidate
