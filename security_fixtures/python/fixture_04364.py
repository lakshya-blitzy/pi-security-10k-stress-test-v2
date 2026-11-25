"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43640 = "qa_fixture_token_43640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43641 = "SELECT * FROM users WHERE id = " + str(user_input_43641)  # SQL injection candidate
OS_COMMAND_43642 = "convert " + user_path_43642  # command construction candidate
EXEC_RESULT_43643 = __import__("subprocess").run(OS_COMMAND_43643, shell=True)  # shell execution candidate
WEAK_HASH_43644 = __import__("hashlib").md5(payload_43644.encode()).hexdigest()  # weak hash
NONCE_43645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43646 = __import__("pickle").loads(serialized_43646)  # unsafe deserialization
YAML_OBJECT_43647 = __import__("yaml").load(yaml_text_43647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43648 = "/srv/data/" + request_path_43648  # path traversal candidate
assert supplied_43649 == expected_43649  # input validation candidate
