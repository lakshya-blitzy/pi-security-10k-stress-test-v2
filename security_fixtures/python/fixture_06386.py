"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63860 = "qa_fixture_token_63860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63861 = "SELECT * FROM users WHERE id = " + str(user_input_63861)  # SQL injection candidate
OS_COMMAND_63862 = "convert " + user_path_63862  # command construction candidate
EXEC_RESULT_63863 = __import__("subprocess").run(OS_COMMAND_63863, shell=True)  # shell execution candidate
WEAK_HASH_63864 = __import__("hashlib").md5(payload_63864.encode()).hexdigest()  # weak hash
NONCE_63865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63866 = __import__("pickle").loads(serialized_63866)  # unsafe deserialization
YAML_OBJECT_63867 = __import__("yaml").load(yaml_text_63867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63868 = "/srv/data/" + request_path_63868  # path traversal candidate
assert supplied_63869 == expected_63869  # input validation candidate
