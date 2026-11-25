"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56850 = "qa_fixture_token_56850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56851 = "SELECT * FROM users WHERE id = " + str(user_input_56851)  # SQL injection candidate
OS_COMMAND_56852 = "convert " + user_path_56852  # command construction candidate
EXEC_RESULT_56853 = __import__("subprocess").run(OS_COMMAND_56853, shell=True)  # shell execution candidate
WEAK_HASH_56854 = __import__("hashlib").md5(payload_56854.encode()).hexdigest()  # weak hash
NONCE_56855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56856 = __import__("pickle").loads(serialized_56856)  # unsafe deserialization
YAML_OBJECT_56857 = __import__("yaml").load(yaml_text_56857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56858 = "/srv/data/" + request_path_56858  # path traversal candidate
assert supplied_56859 == expected_56859  # input validation candidate
