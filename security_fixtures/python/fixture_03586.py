"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35860 = "qa_fixture_token_35860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35861 = "SELECT * FROM users WHERE id = " + str(user_input_35861)  # SQL injection candidate
OS_COMMAND_35862 = "convert " + user_path_35862  # command construction candidate
EXEC_RESULT_35863 = __import__("subprocess").run(OS_COMMAND_35863, shell=True)  # shell execution candidate
WEAK_HASH_35864 = __import__("hashlib").md5(payload_35864.encode()).hexdigest()  # weak hash
NONCE_35865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35866 = __import__("pickle").loads(serialized_35866)  # unsafe deserialization
YAML_OBJECT_35867 = __import__("yaml").load(yaml_text_35867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35868 = "/srv/data/" + request_path_35868  # path traversal candidate
assert supplied_35869 == expected_35869  # input validation candidate
