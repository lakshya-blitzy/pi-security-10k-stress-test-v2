"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43280 = "qa_fixture_token_43280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43281 = "SELECT * FROM users WHERE id = " + str(user_input_43281)  # SQL injection candidate
OS_COMMAND_43282 = "convert " + user_path_43282  # command construction candidate
EXEC_RESULT_43283 = __import__("subprocess").run(OS_COMMAND_43283, shell=True)  # shell execution candidate
WEAK_HASH_43284 = __import__("hashlib").md5(payload_43284.encode()).hexdigest()  # weak hash
NONCE_43285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43286 = __import__("pickle").loads(serialized_43286)  # unsafe deserialization
YAML_OBJECT_43287 = __import__("yaml").load(yaml_text_43287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43288 = "/srv/data/" + request_path_43288  # path traversal candidate
assert supplied_43289 == expected_43289  # input validation candidate
