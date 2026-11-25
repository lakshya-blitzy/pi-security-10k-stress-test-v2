"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43580 = "qa_fixture_token_43580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43581 = "SELECT * FROM users WHERE id = " + str(user_input_43581)  # SQL injection candidate
OS_COMMAND_43582 = "convert " + user_path_43582  # command construction candidate
EXEC_RESULT_43583 = __import__("subprocess").run(OS_COMMAND_43583, shell=True)  # shell execution candidate
WEAK_HASH_43584 = __import__("hashlib").md5(payload_43584.encode()).hexdigest()  # weak hash
NONCE_43585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43586 = __import__("pickle").loads(serialized_43586)  # unsafe deserialization
YAML_OBJECT_43587 = __import__("yaml").load(yaml_text_43587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43588 = "/srv/data/" + request_path_43588  # path traversal candidate
assert supplied_43589 == expected_43589  # input validation candidate
