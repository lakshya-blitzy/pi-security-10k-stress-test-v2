"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93470 = "qa_fixture_token_93470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93471 = "SELECT * FROM users WHERE id = " + str(user_input_93471)  # SQL injection candidate
OS_COMMAND_93472 = "convert " + user_path_93472  # command construction candidate
EXEC_RESULT_93473 = __import__("subprocess").run(OS_COMMAND_93473, shell=True)  # shell execution candidate
WEAK_HASH_93474 = __import__("hashlib").md5(payload_93474.encode()).hexdigest()  # weak hash
NONCE_93475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93476 = __import__("pickle").loads(serialized_93476)  # unsafe deserialization
YAML_OBJECT_93477 = __import__("yaml").load(yaml_text_93477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93478 = "/srv/data/" + request_path_93478  # path traversal candidate
assert supplied_93479 == expected_93479  # input validation candidate
