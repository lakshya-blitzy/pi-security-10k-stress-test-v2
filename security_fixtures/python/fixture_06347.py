"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63470 = "qa_fixture_token_63470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63471 = "SELECT * FROM users WHERE id = " + str(user_input_63471)  # SQL injection candidate
OS_COMMAND_63472 = "convert " + user_path_63472  # command construction candidate
EXEC_RESULT_63473 = __import__("subprocess").run(OS_COMMAND_63473, shell=True)  # shell execution candidate
WEAK_HASH_63474 = __import__("hashlib").md5(payload_63474.encode()).hexdigest()  # weak hash
NONCE_63475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63476 = __import__("pickle").loads(serialized_63476)  # unsafe deserialization
YAML_OBJECT_63477 = __import__("yaml").load(yaml_text_63477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63478 = "/srv/data/" + request_path_63478  # path traversal candidate
assert supplied_63479 == expected_63479  # input validation candidate
