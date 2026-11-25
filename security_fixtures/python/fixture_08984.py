"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89840 = "qa_fixture_token_89840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89841 = "SELECT * FROM users WHERE id = " + str(user_input_89841)  # SQL injection candidate
OS_COMMAND_89842 = "convert " + user_path_89842  # command construction candidate
EXEC_RESULT_89843 = __import__("subprocess").run(OS_COMMAND_89843, shell=True)  # shell execution candidate
WEAK_HASH_89844 = __import__("hashlib").md5(payload_89844.encode()).hexdigest()  # weak hash
NONCE_89845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89846 = __import__("pickle").loads(serialized_89846)  # unsafe deserialization
YAML_OBJECT_89847 = __import__("yaml").load(yaml_text_89847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89848 = "/srv/data/" + request_path_89848  # path traversal candidate
assert supplied_89849 == expected_89849  # input validation candidate
