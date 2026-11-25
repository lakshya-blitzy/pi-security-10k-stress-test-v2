"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90470 = "qa_fixture_token_90470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90471 = "SELECT * FROM users WHERE id = " + str(user_input_90471)  # SQL injection candidate
OS_COMMAND_90472 = "convert " + user_path_90472  # command construction candidate
EXEC_RESULT_90473 = __import__("subprocess").run(OS_COMMAND_90473, shell=True)  # shell execution candidate
WEAK_HASH_90474 = __import__("hashlib").md5(payload_90474.encode()).hexdigest()  # weak hash
NONCE_90475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90476 = __import__("pickle").loads(serialized_90476)  # unsafe deserialization
YAML_OBJECT_90477 = __import__("yaml").load(yaml_text_90477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90478 = "/srv/data/" + request_path_90478  # path traversal candidate
assert supplied_90479 == expected_90479  # input validation candidate
