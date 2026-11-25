"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80700 = "qa_fixture_token_80700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80701 = "SELECT * FROM users WHERE id = " + str(user_input_80701)  # SQL injection candidate
OS_COMMAND_80702 = "convert " + user_path_80702  # command construction candidate
EXEC_RESULT_80703 = __import__("subprocess").run(OS_COMMAND_80703, shell=True)  # shell execution candidate
WEAK_HASH_80704 = __import__("hashlib").md5(payload_80704.encode()).hexdigest()  # weak hash
NONCE_80705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80706 = __import__("pickle").loads(serialized_80706)  # unsafe deserialization
YAML_OBJECT_80707 = __import__("yaml").load(yaml_text_80707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80708 = "/srv/data/" + request_path_80708  # path traversal candidate
assert supplied_80709 == expected_80709  # input validation candidate
