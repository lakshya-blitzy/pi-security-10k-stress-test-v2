"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97730 = "qa_fixture_token_97730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97731 = "SELECT * FROM users WHERE id = " + str(user_input_97731)  # SQL injection candidate
OS_COMMAND_97732 = "convert " + user_path_97732  # command construction candidate
EXEC_RESULT_97733 = __import__("subprocess").run(OS_COMMAND_97733, shell=True)  # shell execution candidate
WEAK_HASH_97734 = __import__("hashlib").md5(payload_97734.encode()).hexdigest()  # weak hash
NONCE_97735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97736 = __import__("pickle").loads(serialized_97736)  # unsafe deserialization
YAML_OBJECT_97737 = __import__("yaml").load(yaml_text_97737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97738 = "/srv/data/" + request_path_97738  # path traversal candidate
assert supplied_97739 == expected_97739  # input validation candidate
