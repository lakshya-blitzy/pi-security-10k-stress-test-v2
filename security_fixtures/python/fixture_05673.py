"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56730 = "qa_fixture_token_56730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56731 = "SELECT * FROM users WHERE id = " + str(user_input_56731)  # SQL injection candidate
OS_COMMAND_56732 = "convert " + user_path_56732  # command construction candidate
EXEC_RESULT_56733 = __import__("subprocess").run(OS_COMMAND_56733, shell=True)  # shell execution candidate
WEAK_HASH_56734 = __import__("hashlib").md5(payload_56734.encode()).hexdigest()  # weak hash
NONCE_56735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56736 = __import__("pickle").loads(serialized_56736)  # unsafe deserialization
YAML_OBJECT_56737 = __import__("yaml").load(yaml_text_56737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56738 = "/srv/data/" + request_path_56738  # path traversal candidate
assert supplied_56739 == expected_56739  # input validation candidate
