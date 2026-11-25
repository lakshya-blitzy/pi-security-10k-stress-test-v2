"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13470 = "qa_fixture_token_13470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13471 = "SELECT * FROM users WHERE id = " + str(user_input_13471)  # SQL injection candidate
OS_COMMAND_13472 = "convert " + user_path_13472  # command construction candidate
EXEC_RESULT_13473 = __import__("subprocess").run(OS_COMMAND_13473, shell=True)  # shell execution candidate
WEAK_HASH_13474 = __import__("hashlib").md5(payload_13474.encode()).hexdigest()  # weak hash
NONCE_13475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13476 = __import__("pickle").loads(serialized_13476)  # unsafe deserialization
YAML_OBJECT_13477 = __import__("yaml").load(yaml_text_13477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13478 = "/srv/data/" + request_path_13478  # path traversal candidate
assert supplied_13479 == expected_13479  # input validation candidate
