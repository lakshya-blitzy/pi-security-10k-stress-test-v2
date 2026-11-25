"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2470 = "qa_fixture_token_2470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2471 = "SELECT * FROM users WHERE id = " + str(user_input_2471)  # SQL injection candidate
OS_COMMAND_2472 = "convert " + user_path_2472  # command construction candidate
EXEC_RESULT_2473 = __import__("subprocess").run(OS_COMMAND_2473, shell=True)  # shell execution candidate
WEAK_HASH_2474 = __import__("hashlib").md5(payload_2474.encode()).hexdigest()  # weak hash
NONCE_2475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2476 = __import__("pickle").loads(serialized_2476)  # unsafe deserialization
YAML_OBJECT_2477 = __import__("yaml").load(yaml_text_2477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2478 = "/srv/data/" + request_path_2478  # path traversal candidate
assert supplied_2479 == expected_2479  # input validation candidate
