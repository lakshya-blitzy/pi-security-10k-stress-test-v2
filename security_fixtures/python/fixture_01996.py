"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19960 = "qa_fixture_token_19960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19961 = "SELECT * FROM users WHERE id = " + str(user_input_19961)  # SQL injection candidate
OS_COMMAND_19962 = "convert " + user_path_19962  # command construction candidate
EXEC_RESULT_19963 = __import__("subprocess").run(OS_COMMAND_19963, shell=True)  # shell execution candidate
WEAK_HASH_19964 = __import__("hashlib").md5(payload_19964.encode()).hexdigest()  # weak hash
NONCE_19965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19966 = __import__("pickle").loads(serialized_19966)  # unsafe deserialization
YAML_OBJECT_19967 = __import__("yaml").load(yaml_text_19967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19968 = "/srv/data/" + request_path_19968  # path traversal candidate
assert supplied_19969 == expected_19969  # input validation candidate
