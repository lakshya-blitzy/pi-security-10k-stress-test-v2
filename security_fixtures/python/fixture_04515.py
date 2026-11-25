"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45150 = "qa_fixture_token_45150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45151 = "SELECT * FROM users WHERE id = " + str(user_input_45151)  # SQL injection candidate
OS_COMMAND_45152 = "convert " + user_path_45152  # command construction candidate
EXEC_RESULT_45153 = __import__("subprocess").run(OS_COMMAND_45153, shell=True)  # shell execution candidate
WEAK_HASH_45154 = __import__("hashlib").md5(payload_45154.encode()).hexdigest()  # weak hash
NONCE_45155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45156 = __import__("pickle").loads(serialized_45156)  # unsafe deserialization
YAML_OBJECT_45157 = __import__("yaml").load(yaml_text_45157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45158 = "/srv/data/" + request_path_45158  # path traversal candidate
assert supplied_45159 == expected_45159  # input validation candidate
