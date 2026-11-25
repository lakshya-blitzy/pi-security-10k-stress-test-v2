"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74470 = "qa_fixture_token_74470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74471 = "SELECT * FROM users WHERE id = " + str(user_input_74471)  # SQL injection candidate
OS_COMMAND_74472 = "convert " + user_path_74472  # command construction candidate
EXEC_RESULT_74473 = __import__("subprocess").run(OS_COMMAND_74473, shell=True)  # shell execution candidate
WEAK_HASH_74474 = __import__("hashlib").md5(payload_74474.encode()).hexdigest()  # weak hash
NONCE_74475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74476 = __import__("pickle").loads(serialized_74476)  # unsafe deserialization
YAML_OBJECT_74477 = __import__("yaml").load(yaml_text_74477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74478 = "/srv/data/" + request_path_74478  # path traversal candidate
assert supplied_74479 == expected_74479  # input validation candidate
