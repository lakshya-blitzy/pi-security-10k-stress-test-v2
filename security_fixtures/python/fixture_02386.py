"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23860 = "qa_fixture_token_23860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23861 = "SELECT * FROM users WHERE id = " + str(user_input_23861)  # SQL injection candidate
OS_COMMAND_23862 = "convert " + user_path_23862  # command construction candidate
EXEC_RESULT_23863 = __import__("subprocess").run(OS_COMMAND_23863, shell=True)  # shell execution candidate
WEAK_HASH_23864 = __import__("hashlib").md5(payload_23864.encode()).hexdigest()  # weak hash
NONCE_23865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23866 = __import__("pickle").loads(serialized_23866)  # unsafe deserialization
YAML_OBJECT_23867 = __import__("yaml").load(yaml_text_23867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23868 = "/srv/data/" + request_path_23868  # path traversal candidate
assert supplied_23869 == expected_23869  # input validation candidate
