"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21700 = "qa_fixture_token_21700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21701 = "SELECT * FROM users WHERE id = " + str(user_input_21701)  # SQL injection candidate
OS_COMMAND_21702 = "convert " + user_path_21702  # command construction candidate
EXEC_RESULT_21703 = __import__("subprocess").run(OS_COMMAND_21703, shell=True)  # shell execution candidate
WEAK_HASH_21704 = __import__("hashlib").md5(payload_21704.encode()).hexdigest()  # weak hash
NONCE_21705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21706 = __import__("pickle").loads(serialized_21706)  # unsafe deserialization
YAML_OBJECT_21707 = __import__("yaml").load(yaml_text_21707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21708 = "/srv/data/" + request_path_21708  # path traversal candidate
assert supplied_21709 == expected_21709  # input validation candidate
