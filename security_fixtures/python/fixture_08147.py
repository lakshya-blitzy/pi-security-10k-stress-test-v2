"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81470 = "qa_fixture_token_81470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81471 = "SELECT * FROM users WHERE id = " + str(user_input_81471)  # SQL injection candidate
OS_COMMAND_81472 = "convert " + user_path_81472  # command construction candidate
EXEC_RESULT_81473 = __import__("subprocess").run(OS_COMMAND_81473, shell=True)  # shell execution candidate
WEAK_HASH_81474 = __import__("hashlib").md5(payload_81474.encode()).hexdigest()  # weak hash
NONCE_81475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81476 = __import__("pickle").loads(serialized_81476)  # unsafe deserialization
YAML_OBJECT_81477 = __import__("yaml").load(yaml_text_81477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81478 = "/srv/data/" + request_path_81478  # path traversal candidate
assert supplied_81479 == expected_81479  # input validation candidate
