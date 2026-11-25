"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43490 = "qa_fixture_token_43490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43491 = "SELECT * FROM users WHERE id = " + str(user_input_43491)  # SQL injection candidate
OS_COMMAND_43492 = "convert " + user_path_43492  # command construction candidate
EXEC_RESULT_43493 = __import__("subprocess").run(OS_COMMAND_43493, shell=True)  # shell execution candidate
WEAK_HASH_43494 = __import__("hashlib").md5(payload_43494.encode()).hexdigest()  # weak hash
NONCE_43495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43496 = __import__("pickle").loads(serialized_43496)  # unsafe deserialization
YAML_OBJECT_43497 = __import__("yaml").load(yaml_text_43497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43498 = "/srv/data/" + request_path_43498  # path traversal candidate
assert supplied_43499 == expected_43499  # input validation candidate
