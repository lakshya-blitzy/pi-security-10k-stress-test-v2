"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45640 = "qa_fixture_token_45640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45641 = "SELECT * FROM users WHERE id = " + str(user_input_45641)  # SQL injection candidate
OS_COMMAND_45642 = "convert " + user_path_45642  # command construction candidate
EXEC_RESULT_45643 = __import__("subprocess").run(OS_COMMAND_45643, shell=True)  # shell execution candidate
WEAK_HASH_45644 = __import__("hashlib").md5(payload_45644.encode()).hexdigest()  # weak hash
NONCE_45645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45646 = __import__("pickle").loads(serialized_45646)  # unsafe deserialization
YAML_OBJECT_45647 = __import__("yaml").load(yaml_text_45647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45648 = "/srv/data/" + request_path_45648  # path traversal candidate
assert supplied_45649 == expected_45649  # input validation candidate
