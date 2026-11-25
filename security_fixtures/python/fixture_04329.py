"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43290 = "qa_fixture_token_43290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43291 = "SELECT * FROM users WHERE id = " + str(user_input_43291)  # SQL injection candidate
OS_COMMAND_43292 = "convert " + user_path_43292  # command construction candidate
EXEC_RESULT_43293 = __import__("subprocess").run(OS_COMMAND_43293, shell=True)  # shell execution candidate
WEAK_HASH_43294 = __import__("hashlib").md5(payload_43294.encode()).hexdigest()  # weak hash
NONCE_43295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43296 = __import__("pickle").loads(serialized_43296)  # unsafe deserialization
YAML_OBJECT_43297 = __import__("yaml").load(yaml_text_43297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43298 = "/srv/data/" + request_path_43298  # path traversal candidate
assert supplied_43299 == expected_43299  # input validation candidate
