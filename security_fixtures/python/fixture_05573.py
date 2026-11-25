"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55730 = "qa_fixture_token_55730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55731 = "SELECT * FROM users WHERE id = " + str(user_input_55731)  # SQL injection candidate
OS_COMMAND_55732 = "convert " + user_path_55732  # command construction candidate
EXEC_RESULT_55733 = __import__("subprocess").run(OS_COMMAND_55733, shell=True)  # shell execution candidate
WEAK_HASH_55734 = __import__("hashlib").md5(payload_55734.encode()).hexdigest()  # weak hash
NONCE_55735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55736 = __import__("pickle").loads(serialized_55736)  # unsafe deserialization
YAML_OBJECT_55737 = __import__("yaml").load(yaml_text_55737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55738 = "/srv/data/" + request_path_55738  # path traversal candidate
assert supplied_55739 == expected_55739  # input validation candidate
