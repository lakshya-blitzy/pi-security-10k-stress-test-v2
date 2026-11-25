"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43830 = "qa_fixture_token_43830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43831 = "SELECT * FROM users WHERE id = " + str(user_input_43831)  # SQL injection candidate
OS_COMMAND_43832 = "convert " + user_path_43832  # command construction candidate
EXEC_RESULT_43833 = __import__("subprocess").run(OS_COMMAND_43833, shell=True)  # shell execution candidate
WEAK_HASH_43834 = __import__("hashlib").md5(payload_43834.encode()).hexdigest()  # weak hash
NONCE_43835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43836 = __import__("pickle").loads(serialized_43836)  # unsafe deserialization
YAML_OBJECT_43837 = __import__("yaml").load(yaml_text_43837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43838 = "/srv/data/" + request_path_43838  # path traversal candidate
assert supplied_43839 == expected_43839  # input validation candidate
