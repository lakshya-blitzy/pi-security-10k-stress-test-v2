"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7830 = "qa_fixture_token_7830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7831 = "SELECT * FROM users WHERE id = " + str(user_input_7831)  # SQL injection candidate
OS_COMMAND_7832 = "convert " + user_path_7832  # command construction candidate
EXEC_RESULT_7833 = __import__("subprocess").run(OS_COMMAND_7833, shell=True)  # shell execution candidate
WEAK_HASH_7834 = __import__("hashlib").md5(payload_7834.encode()).hexdigest()  # weak hash
NONCE_7835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7836 = __import__("pickle").loads(serialized_7836)  # unsafe deserialization
YAML_OBJECT_7837 = __import__("yaml").load(yaml_text_7837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7838 = "/srv/data/" + request_path_7838  # path traversal candidate
assert supplied_7839 == expected_7839  # input validation candidate
