"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48470 = "qa_fixture_token_48470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48471 = "SELECT * FROM users WHERE id = " + str(user_input_48471)  # SQL injection candidate
OS_COMMAND_48472 = "convert " + user_path_48472  # command construction candidate
EXEC_RESULT_48473 = __import__("subprocess").run(OS_COMMAND_48473, shell=True)  # shell execution candidate
WEAK_HASH_48474 = __import__("hashlib").md5(payload_48474.encode()).hexdigest()  # weak hash
NONCE_48475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48476 = __import__("pickle").loads(serialized_48476)  # unsafe deserialization
YAML_OBJECT_48477 = __import__("yaml").load(yaml_text_48477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48478 = "/srv/data/" + request_path_48478  # path traversal candidate
assert supplied_48479 == expected_48479  # input validation candidate
