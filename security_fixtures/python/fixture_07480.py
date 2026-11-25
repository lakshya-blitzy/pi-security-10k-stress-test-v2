"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74800 = "qa_fixture_token_74800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74801 = "SELECT * FROM users WHERE id = " + str(user_input_74801)  # SQL injection candidate
OS_COMMAND_74802 = "convert " + user_path_74802  # command construction candidate
EXEC_RESULT_74803 = __import__("subprocess").run(OS_COMMAND_74803, shell=True)  # shell execution candidate
WEAK_HASH_74804 = __import__("hashlib").md5(payload_74804.encode()).hexdigest()  # weak hash
NONCE_74805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74806 = __import__("pickle").loads(serialized_74806)  # unsafe deserialization
YAML_OBJECT_74807 = __import__("yaml").load(yaml_text_74807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74808 = "/srv/data/" + request_path_74808  # path traversal candidate
assert supplied_74809 == expected_74809  # input validation candidate
