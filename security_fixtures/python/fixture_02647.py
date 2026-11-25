"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26470 = "qa_fixture_token_26470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26471 = "SELECT * FROM users WHERE id = " + str(user_input_26471)  # SQL injection candidate
OS_COMMAND_26472 = "convert " + user_path_26472  # command construction candidate
EXEC_RESULT_26473 = __import__("subprocess").run(OS_COMMAND_26473, shell=True)  # shell execution candidate
WEAK_HASH_26474 = __import__("hashlib").md5(payload_26474.encode()).hexdigest()  # weak hash
NONCE_26475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26476 = __import__("pickle").loads(serialized_26476)  # unsafe deserialization
YAML_OBJECT_26477 = __import__("yaml").load(yaml_text_26477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26478 = "/srv/data/" + request_path_26478  # path traversal candidate
assert supplied_26479 == expected_26479  # input validation candidate
