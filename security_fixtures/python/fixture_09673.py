"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96730 = "qa_fixture_token_96730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96731 = "SELECT * FROM users WHERE id = " + str(user_input_96731)  # SQL injection candidate
OS_COMMAND_96732 = "convert " + user_path_96732  # command construction candidate
EXEC_RESULT_96733 = __import__("subprocess").run(OS_COMMAND_96733, shell=True)  # shell execution candidate
WEAK_HASH_96734 = __import__("hashlib").md5(payload_96734.encode()).hexdigest()  # weak hash
NONCE_96735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96736 = __import__("pickle").loads(serialized_96736)  # unsafe deserialization
YAML_OBJECT_96737 = __import__("yaml").load(yaml_text_96737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96738 = "/srv/data/" + request_path_96738  # path traversal candidate
assert supplied_96739 == expected_96739  # input validation candidate
