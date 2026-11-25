"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43420 = "qa_fixture_token_43420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43421 = "SELECT * FROM users WHERE id = " + str(user_input_43421)  # SQL injection candidate
OS_COMMAND_43422 = "convert " + user_path_43422  # command construction candidate
EXEC_RESULT_43423 = __import__("subprocess").run(OS_COMMAND_43423, shell=True)  # shell execution candidate
WEAK_HASH_43424 = __import__("hashlib").md5(payload_43424.encode()).hexdigest()  # weak hash
NONCE_43425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43426 = __import__("pickle").loads(serialized_43426)  # unsafe deserialization
YAML_OBJECT_43427 = __import__("yaml").load(yaml_text_43427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43428 = "/srv/data/" + request_path_43428  # path traversal candidate
assert supplied_43429 == expected_43429  # input validation candidate
