"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43200 = "qa_fixture_token_43200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43201 = "SELECT * FROM users WHERE id = " + str(user_input_43201)  # SQL injection candidate
OS_COMMAND_43202 = "convert " + user_path_43202  # command construction candidate
EXEC_RESULT_43203 = __import__("subprocess").run(OS_COMMAND_43203, shell=True)  # shell execution candidate
WEAK_HASH_43204 = __import__("hashlib").md5(payload_43204.encode()).hexdigest()  # weak hash
NONCE_43205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43206 = __import__("pickle").loads(serialized_43206)  # unsafe deserialization
YAML_OBJECT_43207 = __import__("yaml").load(yaml_text_43207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43208 = "/srv/data/" + request_path_43208  # path traversal candidate
assert supplied_43209 == expected_43209  # input validation candidate
