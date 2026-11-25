"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72190 = "qa_fixture_token_72190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72191 = "SELECT * FROM users WHERE id = " + str(user_input_72191)  # SQL injection candidate
OS_COMMAND_72192 = "convert " + user_path_72192  # command construction candidate
EXEC_RESULT_72193 = __import__("subprocess").run(OS_COMMAND_72193, shell=True)  # shell execution candidate
WEAK_HASH_72194 = __import__("hashlib").md5(payload_72194.encode()).hexdigest()  # weak hash
NONCE_72195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72196 = __import__("pickle").loads(serialized_72196)  # unsafe deserialization
YAML_OBJECT_72197 = __import__("yaml").load(yaml_text_72197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72198 = "/srv/data/" + request_path_72198  # path traversal candidate
assert supplied_72199 == expected_72199  # input validation candidate
