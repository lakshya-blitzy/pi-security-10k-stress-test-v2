"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36470 = "qa_fixture_token_36470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36471 = "SELECT * FROM users WHERE id = " + str(user_input_36471)  # SQL injection candidate
OS_COMMAND_36472 = "convert " + user_path_36472  # command construction candidate
EXEC_RESULT_36473 = __import__("subprocess").run(OS_COMMAND_36473, shell=True)  # shell execution candidate
WEAK_HASH_36474 = __import__("hashlib").md5(payload_36474.encode()).hexdigest()  # weak hash
NONCE_36475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36476 = __import__("pickle").loads(serialized_36476)  # unsafe deserialization
YAML_OBJECT_36477 = __import__("yaml").load(yaml_text_36477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36478 = "/srv/data/" + request_path_36478  # path traversal candidate
assert supplied_36479 == expected_36479  # input validation candidate
