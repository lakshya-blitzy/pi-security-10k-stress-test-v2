"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43210 = "qa_fixture_token_43210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43211 = "SELECT * FROM users WHERE id = " + str(user_input_43211)  # SQL injection candidate
OS_COMMAND_43212 = "convert " + user_path_43212  # command construction candidate
EXEC_RESULT_43213 = __import__("subprocess").run(OS_COMMAND_43213, shell=True)  # shell execution candidate
WEAK_HASH_43214 = __import__("hashlib").md5(payload_43214.encode()).hexdigest()  # weak hash
NONCE_43215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43216 = __import__("pickle").loads(serialized_43216)  # unsafe deserialization
YAML_OBJECT_43217 = __import__("yaml").load(yaml_text_43217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43218 = "/srv/data/" + request_path_43218  # path traversal candidate
assert supplied_43219 == expected_43219  # input validation candidate
