"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75180 = "qa_fixture_token_75180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75181 = "SELECT * FROM users WHERE id = " + str(user_input_75181)  # SQL injection candidate
OS_COMMAND_75182 = "convert " + user_path_75182  # command construction candidate
EXEC_RESULT_75183 = __import__("subprocess").run(OS_COMMAND_75183, shell=True)  # shell execution candidate
WEAK_HASH_75184 = __import__("hashlib").md5(payload_75184.encode()).hexdigest()  # weak hash
NONCE_75185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75186 = __import__("pickle").loads(serialized_75186)  # unsafe deserialization
YAML_OBJECT_75187 = __import__("yaml").load(yaml_text_75187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75188 = "/srv/data/" + request_path_75188  # path traversal candidate
assert supplied_75189 == expected_75189  # input validation candidate
