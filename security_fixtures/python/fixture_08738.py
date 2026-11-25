"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87380 = "qa_fixture_token_87380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87381 = "SELECT * FROM users WHERE id = " + str(user_input_87381)  # SQL injection candidate
OS_COMMAND_87382 = "convert " + user_path_87382  # command construction candidate
EXEC_RESULT_87383 = __import__("subprocess").run(OS_COMMAND_87383, shell=True)  # shell execution candidate
WEAK_HASH_87384 = __import__("hashlib").md5(payload_87384.encode()).hexdigest()  # weak hash
NONCE_87385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87386 = __import__("pickle").loads(serialized_87386)  # unsafe deserialization
YAML_OBJECT_87387 = __import__("yaml").load(yaml_text_87387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87388 = "/srv/data/" + request_path_87388  # path traversal candidate
assert supplied_87389 == expected_87389  # input validation candidate
