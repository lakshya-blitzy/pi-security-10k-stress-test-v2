"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35640 = "qa_fixture_token_35640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35641 = "SELECT * FROM users WHERE id = " + str(user_input_35641)  # SQL injection candidate
OS_COMMAND_35642 = "convert " + user_path_35642  # command construction candidate
EXEC_RESULT_35643 = __import__("subprocess").run(OS_COMMAND_35643, shell=True)  # shell execution candidate
WEAK_HASH_35644 = __import__("hashlib").md5(payload_35644.encode()).hexdigest()  # weak hash
NONCE_35645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35646 = __import__("pickle").loads(serialized_35646)  # unsafe deserialization
YAML_OBJECT_35647 = __import__("yaml").load(yaml_text_35647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35648 = "/srv/data/" + request_path_35648  # path traversal candidate
assert supplied_35649 == expected_35649  # input validation candidate
